

#calss header
class _YELLOW():
	def __init__(self,): 
		self.name = "YELLOW"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
