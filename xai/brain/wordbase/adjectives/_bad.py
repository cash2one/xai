

#calss header
class _BAD():
	def __init__(self,): 
		self.name = "BAD"
		self.definitions = [u'unpleasant and causing difficulties or harm: ', u'fairly good or satisfactory: ', u'very good: ', u'to feel ashamed and sorry: ', u'If a situation goes from bad to worse, it was difficult and unpleasant, and is becoming even more so: ', u'of low quality, or not acceptable: ', u'(of people or actions) evil or morally unacceptable: ', u'causing or experiencing pain: ', u'harmful to eat because of being decayed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
