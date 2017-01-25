

#calss header
class _UNLIKELY():
	def __init__(self,): 
		self.name = "UNLIKELY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
