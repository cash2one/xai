

#calss header
class _QUALITY():
	def __init__(self,): 
		self.name = "QUALITY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
