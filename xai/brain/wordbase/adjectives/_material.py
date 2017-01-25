

#calss header
class _MATERIAL():
	def __init__(self,): 
		self.name = "MATERIAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
