

#calss header
class _SCIENTIFIC():
	def __init__(self,): 
		self.name = "SCIENTIFIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
