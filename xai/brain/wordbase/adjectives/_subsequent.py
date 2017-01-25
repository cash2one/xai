

#calss header
class _SUBSEQUENT():
	def __init__(self,): 
		self.name = "SUBSEQUENT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
