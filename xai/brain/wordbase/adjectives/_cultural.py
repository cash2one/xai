

#calss header
class _CULTURAL():
	def __init__(self,): 
		self.name = "CULTURAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
