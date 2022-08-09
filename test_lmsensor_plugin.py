#!/usr/bin/env python3
import re
import unittest
import lmsensor_plugin
from arcaflow_plugin_sdk import plugin


class LMSensorTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(
            lmsensor_plugin.InputParams(
                10, 1
            )
        )

        plugin.test_object_serialization(
            lmsensor_plugin.SuccessOutput(
                """{
   "iwlwifi_1-virtual-0":{
      "Adapter": "Virtual device",
      "temp1":{
         "temp1_input": 49.000
      }
   },
   "pch_skylake-virtual-0":{
      "Adapter": "Virtual device",
      "temp1":{
         "temp1_input": 47.000
      }
   },
   "acpitz-virtual-0":{
      "Adapter": "Virtual device",
      "temp1":{
         "temp1_input": 52.000,
         "temp1_crit": 128.000
      }
   },
   "coretemp-isa-0000":{
      "Adapter": "ISA adapter",
      "Package id 0":{
         "temp1_input": 53.000,
         "temp1_max": 100.000,
         "temp1_crit": 100.000,
         "temp1_crit_alarm": 0.000
      },
      "Core 0":{
         "temp2_input": 53.000,
         "temp2_max": 100.000,
         "temp2_crit": 100.000,
         "temp2_crit_alarm": 0.000
      },
      "Core 1":{
         "temp3_input": 51.000,
         "temp3_max": 100.000,
         "temp3_crit": 100.000,
         "temp3_crit_alarm": 0.000
      },
      "Core 2":{
         "temp4_input": 50.000,
         "temp4_max": 100.000,
         "temp4_crit": 100.000,
         "temp4_crit_alarm": 0.000
      },
      "Core 3":{
         "temp5_input": 51.000,
         "temp5_max": 100.000,
         "temp5_crit": 100.000,
         "temp5_crit_alarm": 0.000
      }
   },
   "thinkpad-isa-0000":{
      "Adapter": "ISA adapter",
      "fan1":{
         "fan1_input": 0.000
      }
   }
}"""
            )
        )

        plugin.test_object_serialization(
            lmsensor_plugin.ErrorOutput(
                error="This is an error"
            )
        )


if __name__ == '__main__':
    unittest.main()
