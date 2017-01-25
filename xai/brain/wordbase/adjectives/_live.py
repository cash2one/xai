

#calss header
class _LIVE():
	def __init__(self,): 
		self.name = "LIVE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
