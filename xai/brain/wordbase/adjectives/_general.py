

#calss header
class _GENERAL():
	def __init__(self,): 
		self.name = "GENERAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
