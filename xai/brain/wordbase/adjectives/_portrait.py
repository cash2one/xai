

#calss header
class _PORTRAIT():
	def __init__(self,): 
		self.name = "PORTRAIT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
