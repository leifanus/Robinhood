import subprocess
import json


class Robinhood():
	def __init__(self, stock):
		self.stock = stock
		self.parameter_list = ['open', 'high', 'low', 'volume']
		self.command_list = ['curl -v https://api.robinhood.com/fundamentals/' + self.stock + '/ -H "Accept: application/json"']
		# command_list = ['curl -v https://api.robinhood.com/quotes/' + self.stock + '/ -H "Accept: application/json"']

	def quote(self):
		p = subprocess.Popen(self.command_list[0], shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)
		out, err = p.communicate()
		out = json.loads(out)
		# out = out.decode("utf-8")
		for parameter in self.parameter_list:
			print(parameter, out[parameter])

		# print(out["open"])

# curl -v https://api.robinhood.com/fundamentals/MSFT/ \
#    -H "Accept: application/json"

if __name__ == '__main__':
	ticker = input('Type stock ticker: ')
	data = Robinhood(ticker)
	data.quote()