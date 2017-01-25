

#calss header
class _FEMALE():
	def __init__(self,): 
		self.name = "FEMALE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
