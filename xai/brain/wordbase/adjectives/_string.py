

#calss header
class _STRING():
	def __init__(self,): 
		self.name = "STRING"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
