#!/usr/bin/env python3

import sys
import typing
import time
from dataclasses import dataclass
from arcaflow_plugin_sdk import plugin, validation


@dataclass
class InputParams:
    """
    This is the data structure for the input parameters of the step defined below.
    """
    iterations: typing.Annotated[int, validation.min(1)]
    interval: typing.Annotated[int, validation.min(0)]


@dataclass
class SuccessOutput:
    """
    This is the output data structure for the success case.
    """
    message: str


@dataclass
class ErrorOutput:
    """
    This is the output data structure in the error  case.
    """
    error: str


@plugin.step(
    id="lmsensor",
    name="lmsensor plugin",
    description="Run sensors",
    outputs={"success": SuccessOutput, "error": ErrorOutput},
)
def run_sensors(params: InputParams) -> typing.Tuple[str, typing.Union[SuccessOutput, ErrorOutput]]:
    """
    Run sensors for the given number of iterations with the given interval
    in seconds.

    :param params:

    :return: a json with the result
    """
    final_result = ""
    for current in range(params.iterations):
        result = subprocess.run(
            ["/usr/bin/sensors", "-c"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            return "error", ErrorOutput(result.stderr)
        final_result += result.stdout
        time.sleep(params.interval)

    return "success", SuccessOutput(final_result)


if __name__ == "__main__":
    sys.exit(plugin.run(plugin.build_schema(
        # List your step functions here:
        run_sensors,
    )))
