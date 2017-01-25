

#calss header
class _AUTO():
	def __init__(self,): 
		self.name = "AUTO"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
