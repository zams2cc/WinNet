# Author: Moritz Reichert
# Date  : 26.09.2024
import numpy as np


class template(object):
    """
      Class to read a WinNet template file.
    """

    def __init__(self, path):
        """
          Initialize the template class.
        """
        self.path = path


    def read_data(self):
        """
          Read the data from the template file and store it in a dictionary.
        """
        # Create an empty dictionary to store the entries
        self.__entries = {}

        # Read the data from the file
        with open(self.path, 'r') as f:
            self.data = f.readlines()
            for line in self.data:
                if line.strip().startswith('#'):
                    continue

                if line.strip() =="":
                    continue

                key = line.split("=")[0].strip()
                value = line.split("=")[1].strip().replace('"', '').replace("'", "")
                self.__entries[key] = value

    @property
    def entries(self):
        """
          Get the entries of the template file.
        """
        # Check if entry exists.
        #print all attributes of the object
        if not hasattr(self, '_template__entries'):
            self.read_data()
        return self.__entries


    def __getitem__(self, key):
        """
          Get the value of a specific key.
        """
        if not hasattr(self, '_template__entries'):
            self.read_data()
        return self.entries[key]

    def __setitem__(self, key, value):
        """
        Set the value of a specific key.
        """
        if not hasattr(self, '_template__entries'):
            self.read_data()
        self.__entries[key] = value


    def save_template(self, path, winnet_path=None):
        """
          Save the template file.
        """
        with open(path, 'w') as f:
            for key, value in self.entries.items():
                if winnet_path is None:
                    f.write(f"{key} = {value}\n")
                else:
                    entry = str(value).replace("@WINNET@",winnet_path)
                    f.write(f"{key} = {entry}\n")


if __name__ == '__main__':
    # Example:
    path = '/home/mreichert/data/Networks/comparison_winNet/WinNet-dev/par/NSE_comp.par'
    t = template(path)
    print(t["isotopes_file"])
    t.save_template('test.par', winnet_path='../../runs/winnet')