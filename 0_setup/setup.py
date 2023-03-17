import os
import xml.etree.ElementTree as ET

# Set the STORAGE environment variable (Thanks to Paul DeFusco)
try:
    storage = os.environ["STORAGE"]
except:
    if os.path.exists("/etc/hadoop/conf/hive-site.xml"):
        tree = ET.parse("/etc/hadoop/conf/hive-site.xml")
        root = tree.getroot()
        for prop in root.findall("property"):
            if prop.find("name").text == "hive.metastore.warehouse.dir":
                storage = (
                    prop.find("value").text.split("/")[0]
                    + "//"
                    + prop.find("value").text.split("/")[2]
                )
    else:
        storage = "/user/" + os.getenv("HADOOP_USER_NAME")
  #  storage_environment_params = {"STORAGE": storage}
  #  storage_environment = cml.create_environment_variable(storage_environment_params)
    os.environ["STORAGE"] = storage