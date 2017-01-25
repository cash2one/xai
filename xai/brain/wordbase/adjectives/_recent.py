

#calss header
class _RECENT():
	def __init__(self,): 
		self.name = "RECENT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
