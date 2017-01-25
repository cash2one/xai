

#calss header
class _PREGNANT():
	def __init__(self,): 
		self.name = "PREGNANT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
