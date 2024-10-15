def read_data(path: str, tHead: list['str'], paraNumeric: list[int]=[], paraRemove: list[int]=[]) -> list:
  """
    This function will read the named data and give out a list with dicts read from the file.<br/>
    Data line with '?' will not be stored and returned.<br/>
    Can customize for removeing named variable.<br/>
    PARAS:<br/>
    <p>
      path: the path of the data to read<br/>
      tHead: the header of the table to be read<br/>
      paraNumeric: data in the file to be converted to integer<br/>
      varRemove: data in the file required to be removed<br/>
    </p>
    RETURN:<br/>
      A data list read from the file named. Each data line is presented in a dict.
  """
  resData = []
  with open(path, 'r') as data:
    for line in data:
      ldata = line.strip()
      if(ldata):
        ldata = ldata.split(", ")
        if('?' not in ldata and len(ldata) > 1):
          if(paraNumeric):
            for num in paraNumeric:
              ldata[num] = int(ldata[num])
          if(paraRemove): 
            for rem in paraRemove:
              del ldata[rem]
          assert len(ldata) == len(tHead)
          resData.append(dict(zip(tHead, ldata)))
  return resData

def count_frequencies(data: list[dict]) -> dict:
  """
  Statictic the frequence of each attribute in the data.<br/>
  PARAS:<br/>
  <p>
    data: The data in type of list with dict as elements.
  </p>
  RETURN:<br/>
    A dict with statictical data.
  """
  frequency = {}
  for record in data:
    for key, value in record.items():
      if key not in frequency:
        frequency[key] = {}
      if value not in frequency[key]:
        frequency[key][value] = 0
      frequency[key][value] += 1
  return frequency

def get_sorted_list_value(data: dict, key: str|int ,desending=True) -> list:
  """
  Sort the frequence of each attribute in the data by value.<br/>
  PARAS:<br/>
  <p>
    data: The data in type of list with dict as elements.
    key: The key of dict
    desending: True default, return desended list based on number of each value.
  </p>
  RETURN:<br/>
    A sorted data list with tuple (value, numbers).
  """
  return sorted(data[key].items(), key=lambda item: item[1], reverse=desending)

def get_sorted_list_key(data: dict, key: str | int, desending=False) -> list:
    """
    Sort the frequency of each attribute in the data by key.<br/>
    PARAS:<br/>
    <p>
      data: The data in type of list with dict as elements.
      key: The key of dict.
      desending: False by default, return ascending list based on the key.
    </p>
    RETURN:<br/>
      A sorted data list with tuple (value, numbers).
    """
    return sorted(data[key].items(), key=lambda item: item[0], reverse=desending)

