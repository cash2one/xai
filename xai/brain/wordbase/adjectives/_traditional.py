

#calss header
class _TRADITIONAL():
	def __init__(self,): 
		self.name = "TRADITIONAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
