

#calss header
class _EQUAL():
	def __init__(self,): 
		self.name = "EQUAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
