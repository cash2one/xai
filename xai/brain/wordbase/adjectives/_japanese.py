

#calss header
class _JAPANESE():
	def __init__(self,): 
		self.name = "JAPANESE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
