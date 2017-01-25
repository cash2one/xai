

#calss header
class _SOUND():
	def __init__(self,): 
		self.name = "SOUND"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
