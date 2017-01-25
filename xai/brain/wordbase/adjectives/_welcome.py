

#calss header
class _WELCOME():
	def __init__(self,): 
		self.name = "WELCOME"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
