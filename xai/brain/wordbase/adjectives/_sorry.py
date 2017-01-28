

#calss header
class _SORRY():
	def __init__(self,): 
		self.name = "SORRY"
		self.definitions = [u'feeling sadness, sympathy, or disappointment, especially because something unpleasant has happened or been done: ', u'to feel sad because you have a problem and you feel that it is not fair that you are suffering so much: ', u'used to show that something that must be said causes sadness or disappointment: ', u'used to say that you wish you had not done what you have done, especially when you want to be polite to someone you have done something bad to: ', u'used to show politeness when refusing something or disagreeing: ', u'a bad condition or situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
