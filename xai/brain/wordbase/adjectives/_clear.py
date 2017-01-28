

#calss header
class _CLEAR():
	def __init__(self,): 
		self.name = "CLEAR"
		self.definitions = [u'easy to understand, hear, read, or see: ', u'something you say in order to emphasize what you have just said, or to express your authority: ', u'certain, having no doubt, or obvious: ', u'pure or easy to see through, with no marks or areas that are less transparent: ', u'used to describe a pleasant, pure sound: ', u'used to describe something that you remember easily: ', u'not covered or blocked by anything: ', u'not busy or filled by any planned activity: ', u'without being or feeling guilty: ', u'free from confusion; able to think quickly and well: ', u'without problems or difficulties: ', u'used to describe an amount of money that is left after all necessary payments have been made: ', u'not touching something, or away from something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
