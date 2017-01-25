

#calss header
class _FAT():
	def __init__(self,): 
		self.name = "FAT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
