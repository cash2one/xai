

#calss header
class _VETERAN():
	def __init__(self,): 
		self.name = "VETERAN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
