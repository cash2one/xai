

#calss header
class _ORIGINAL():
	def __init__(self,): 
		self.name = "ORIGINAL"
		self.definitions = [u'existing since the beginning, or being the earliest form of something: ', u'An original piece of work, such as a painting, etc. is produced by the artist and not a copy: ', u'not the same as anything or anyone else and therefore special and interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
