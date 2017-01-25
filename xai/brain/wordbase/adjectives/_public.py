

#calss header
class _PUBLIC():
	def __init__(self,): 
		self.name = "PUBLIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
