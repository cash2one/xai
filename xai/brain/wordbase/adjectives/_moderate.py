

#calss header
class _MODERATE():
	def __init__(self,): 
		self.name = "MODERATE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
