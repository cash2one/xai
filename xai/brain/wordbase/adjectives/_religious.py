

#calss header
class _RELIGIOUS():
	def __init__(self,): 
		self.name = "RELIGIOUS"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
