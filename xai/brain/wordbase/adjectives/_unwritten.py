

#calss header
class _UNWRITTEN():
	def __init__(self,): 
		self.name = "UNWRITTEN"
		self.definitions = [u'Something that is unwritten does not exist in a written or printed form: ', u'An unwritten rule or law does not exist officially but people generally accept and obey it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
