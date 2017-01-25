

#calss header
class _HIGH():
	def __init__(self,): 
		self.name = "HIGH"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
