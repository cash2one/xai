

#calss header
class _SOCIAL():
	def __init__(self,): 
		self.name = "SOCIAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
