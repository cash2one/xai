

#calss header
class _ITALIAN():
	def __init__(self,): 
		self.name = "ITALIAN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
