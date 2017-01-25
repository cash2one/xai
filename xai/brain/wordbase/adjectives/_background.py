

#calss header
class _BACKGROUND():
	def __init__(self,): 
		self.name = "BACKGROUND"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
