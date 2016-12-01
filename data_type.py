def data_type(arg):
  
  if isinstance(arg,str):
    return len(arg)
  if arg == None :
    return 'no value'
  if isinstance(arg,bool):
    return arg
  if isinstance(arg,int):
    if arg < 100 :
      return 'less than 100'
    elif arg > 100:
      return 'more than 100'
    else:
      return 'equal to 100'
  if isinstance(arg,list) and len(arg)=>3 :
      return arg[2]
  else:
      None

print data_type(101)
