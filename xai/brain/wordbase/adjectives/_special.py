

#calss header
class _SPECIAL():
	def __init__(self,): 
		self.name = "SPECIAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
