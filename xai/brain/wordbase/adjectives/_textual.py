

#calss header
class _TEXTUAL():
	def __init__(self,): 
		self.name = "TEXTUAL"
		self.definitions = [u'relating to written or printed material', u'related to the way in which something has been written: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
