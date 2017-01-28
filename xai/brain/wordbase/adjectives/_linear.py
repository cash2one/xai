

#calss header
class _LINEAR():
	def __init__(self,): 
		self.name = "LINEAR"
		self.definitions = [u'consisting of or to do with lines: ', u'relating to length, rather than area or volume: ', u'involving a series of events or thoughts in which one follows another one directly: ', u'A linear relationship between two things is direct or clear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
