

#calss header
class _WRONG():
	def __init__(self,): 
		self.name = "WRONG"
		self.definitions = [u'not correct: ', u'If someone is wrong, they are not correct in their judgment or statement about something: ', u"to show by your actions that someone's judgment of you was not correct: ", u'not suitable or correct, or not as it should be: ', u'Something that is wrong is not considered to be socially acceptable or suitable: ', u'If you ask someone what is wrong, you want to know what is worrying or upsetting them: ', u'If something is the wrong way around, the part that should be at the front is at the back: ', u'not considered morally acceptable by most people: ', u'not working correctly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
