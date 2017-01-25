

#calss header
class _ADVANCED():
	def __init__(self,): 
		self.name = "ADVANCED"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
