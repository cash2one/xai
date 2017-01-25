

#calss header
class _EXPERT():
	def __init__(self,): 
		self.name = "EXPERT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
