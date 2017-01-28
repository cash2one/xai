

#calss header
class _LYRIC():
	def __init__(self,): 
		self.name = "LYRIC"
		self.definitions = [u'(especially of poetry and songs) expressing personal thoughts and feelings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
