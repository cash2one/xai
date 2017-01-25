

#calss header
class _WEEKLY():
	def __init__(self,): 
		self.name = "WEEKLY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
