from operator import contains


class FileUtil():
  coins_symbol_list = []
  count = 1000;
  end = None
  def readLines(self):
      with open('C:\\Users\\shirish\\Desktop\\coinslist.json', 'r') as f:
        for line in f:
             if "Symbol" in line:
              line = line[17:];
              line= line[:line.index('"')];
              FileUtil.coins_symbol_list.append("#"+line);
             if "CoinName" in line:
              line = line[19:];
              line = line[:line.index('"')];
              FileUtil.coins_symbol_list.append(line);



fu = FileUtil()
fu.readLines();
print(len(fu.coins_symbol_list))
print(fu.coins_symbol_list)
