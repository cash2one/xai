

#calss header
class _PENSIVE():
	def __init__(self,): 
		self.name = "PENSIVE"
		self.definitions = [u'thinking in a quiet way, often with a serious expression on your face: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
