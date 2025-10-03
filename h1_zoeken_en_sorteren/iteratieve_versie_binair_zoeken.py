def zoek_binair(item, rij):
  links = 0
  rechts = len(rij) - 1
  while links != rechts:
    print(f'{links}, {rechts}')
    midden = (links + rechts)//2
    if rij[midden] < item:
      links = midden + 1
    else:
      rechts = midden
  if rij[links] == item:
    index = links
  else:
    index = -1
  return index