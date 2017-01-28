

#calss header
class _ZIPLOC():
	def __init__(self,): 
		self.name = "ZIPLOC"
		self.definitions = [u'used to describe a type of plastic bag that can be closed firmly by pressing the two edges at the top together, and opened by pulling them apart: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
