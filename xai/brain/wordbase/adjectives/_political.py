

#calss header
class _POLITICAL():
	def __init__(self,): 
		self.name = "POLITICAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
